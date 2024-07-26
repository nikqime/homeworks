function isTeenager(age, hasPermission) {
    if (age < 18 && !hasPermission) {
        return false;
    } else if (age >= 18 && hasPermission) {
        return true;
    }
    return false;
}