from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from collections import Counter
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import roc_curve
from sklearn.model_selection import train_test_split

def model_score(model, X_test, Y_test):
    score = model.score(X_test, Y_test)
    return score

def fpr_and_tpr(model, X_test, Y_test):
    Y_pred = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(Y_test, Y_pred)
    return fpr, tpr

def auc(fpr, tpr):
    auc = metrics.auc(fpr, tpr)
    return auc

def split_data(X, Y, test_size = 0.2, random_state = 42, perform_pca = False):
    """
    Split data into training and test sets.
    """
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=random_state)

    print('Training data count: ', len(X_train))
    print('Testing data count: ', len(X_test))

    if not perform_pca:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    return X_train, X_test, Y_train, Y_test

def check_and_balance(X, Y, balance_threshold=0.5):
    """
    Check if the dataset is imbalanced and perform oversampling if necessary.

    Args:
    X (DataFrame): Feature set.
    Y (Series): Target variable.
    balance_threshold (float): Threshold for class balance.

    Returns:
    X_resampled, Y_resampled (DataFrame/Series): Resampled data if imbalance is detected, 
    else original data.
    """
    # Check the distribution of the target variable
    class_distribution = Counter(Y)

    # Determine if the dataset is imbalanced
    min_class_samples = min(class_distribution.values())
    max_class_samples = max(class_distribution.values())
    is_imbalanced = min_class_samples / max_class_samples < balance_threshold

    if is_imbalanced:
        oversampler = RandomOverSampler(random_state=0)
        X_resampled, Y_resampled = oversampler.fit_resample(X, Y)
        print("Resampled class distribution:", Counter(Y_resampled))
        return X_resampled, Y_resampled
    else:
        print("No significant imbalance detected.")
        return X, Y