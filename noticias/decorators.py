from django.contrib.auth.decorators import user_passes_test, login_required
def admin_required(view_func):
    """
    Decorator for views that checks that the user is logged in and is an administrator,
    redirecting to the log-in page if necessary.
    """
    decorated_view_func = login_required(user_passes_test(
        lambda user: user.is_authenticated and user.groups.filter(name='Administrador').exists(),
        login_url='login'
    )(view_func))
    return decorated_view_func