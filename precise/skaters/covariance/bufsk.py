from precise.skaters.covarianceutil.conventions import X_TYPE
from precise.skaters.covariance.bufskfactory import buf_sk_factory
from precise.skaters.covarianceutil.differencing import d1_factory
from sklearn.covariance import GraphicalLasso, GraphicalLassoCV, LedoitWolf, MinCovDet, OAS, EmpiricalCovariance

# Sklearn


def buf_sk_emp_pcov_d0_n100(y: X_TYPE = None, s: dict = None, n_buffer: int = 100, k=1):
    """ Sklearn empirical covariance based estimator for IID observations """
    assert k == 1
    return buf_sk_factory(cls=EmpiricalCovariance, y=y, s=s, n_buffer=n_buffer, n_emp=2)


def buf_sk_ld_pcov_d0_n100(y: X_TYPE = None, s: dict = None, n_buffer: int = 100, k=1):
    """ Ledoit-Wolf covariance based estimator for IID observations """
    assert k == 1
    return buf_sk_factory(cls=LedoitWolf, y=y, s=s, n_buffer=n_buffer, n_emp=5)


def buf_sk_gl_pcov_d0_n100(y: X_TYPE = None, s: dict = None, n_buffer: int = 100, k=1):
    """ Graphical Lasso covariance based estimator for IID observations """
    assert k == 1
    cls_kwargs = {'tol':1e-2,'max_iter':200}
    return buf_sk_factory(cls=GraphicalLasso, y=y, s=s, n_buffer=n_buffer, n_emp=50, cls_kwargs=cls_kwargs)


def buf_sk_glcv_pcov_d0_n100(y: X_TYPE = None, s: dict = None, n_buffer: int = 100, k=1):
    """ Graphical Lasso CV covariance based estimator for IID observations """
    assert k == 1
    return buf_sk_factory(cls=GraphicalLassoCV, y=y, s=s, n_buffer=n_buffer, n_emp=30)


def buf_sk_mcd_pcov_d0_n100(y: X_TYPE = None, s: dict = None, n_buffer: int = 100, k=1):
    """ Minimumn covariance based estimator for IID observations """
    assert k == 1
    # https://scikit-learn.org/stable/modules/generated/sklearn.covariance.MinCovDet.html#sklearn.covariance.MinCovDet
    return buf_sk_factory(cls=MinCovDet, y=y, s=s, n_buffer=n_buffer, n_emp=10)


def buf_sk_oas_pcov_d0_n100(y: X_TYPE = None, s: dict = None, n_buffer: int = 100, k=1):
    """ OAS based estimator for IID observations """
    #https://arxiv.org/abs/0907.4698
    assert k == 1
    return buf_sk_factory(cls=OAS, y=y, s=s, n_buffer=n_buffer, n_emp=10)


# Differenced versions to be applied to time-series with independent increments


def buf_sk_ec_pcov_d1_n100(y: X_TYPE = None, s: dict = None, n_buffer: int = 100, k=1):
    assert k == 1
    return d1_factory(f=buf_sk_emp_pcov_d0_n100, y=y, s=s, n_buffer=n_buffer)


def buf_sk_ld_pcov_d1_n100(y: X_TYPE = None, s: dict = None, n_buffer: int = 100, k=1):
    """ Ledoit-Wolf covariance based estimator for IID changes """
    assert k == 1
    return d1_factory(f=buf_sk_ld_pcov_d0_n100, y=y, s=s, n_buffer=n_buffer, k=1)


def buf_sk_oas_pcov_d1_n100(y: X_TYPE = None, s: dict = None, n_buffer: int = 100, k=1):
    """ OAS based estimator for IID changes  """
    assert k == 1
    return d1_factory(f=buf_sk_oas_pcov_d0_n100, y=y, s=s, n_buffer=n_buffer, k=1)


def buf_sk_gl_pcov_d1_n100(y: X_TYPE = None, s: dict = None, n_buffer: int = 100, k=1):
    """ GL based estimator for IID changes  """
    assert k == 1
    return d1_factory(f=buf_sk_gl_pcov_d0_n100, y=y, s=s, n_buffer=n_buffer)


def buf_sk_glcv_pcov_d1_n100(y: X_TYPE = None, s: dict = None, n_buffer: int = 100, k=1):
    """ GL CV based estimator for IID changes  """
    assert k == 1
    return d1_factory(f=buf_sk_glcv_pcov_d0_n100, y=y, s=s, n_buffer=n_buffer, k=1)


def buf_sk_mcd_pcov_d1_n100(y: X_TYPE = None, s: dict = None, n_buffer: int = 100, k=1):
    """ Minimumn covariance based estimator for IID changes """
    assert k == 1
    # https://scikit-learn.org/stable/modules/generated/sklearn.covariance.MinCovDet.html#sklearn.covariance.MinCovDet
    return d1_factory(f=buf_sk_mcd_pcov_d0_n100, y=y, s=s, n_buffer=n_buffer, k=1)


BUF_SK_D0_SKATERS = [buf_sk_emp_pcov_d0_n100, buf_sk_ld_pcov_d0_n100, buf_sk_gl_pcov_d0_n100, buf_sk_glcv_pcov_d0_n100,
                     buf_sk_mcd_pcov_d0_n100, buf_sk_oas_pcov_d0_n100]

BUF_SK_D1_SKATERS = [buf_sk_ec_pcov_d1_n100, buf_sk_ld_pcov_d1_n100, buf_sk_gl_pcov_d1_n100, buf_sk_glcv_pcov_d1_n100,
                     buf_sk_mcd_pcov_d1_n100, buf_sk_oas_pcov_d1_n100]


if __name__=='__main__':
    from precise.whereami import url_from_skater_name
    print(url_from_skater_name(name='buf_sk_mcd_pcov_d1_n100'))