import sentry_sdk


dsn = "https://2ee2ecc719182a02f66fcca56bec72b7@o4506084321984512.ingest.sentry.io/4506089257172992"
traces_sample_rate = 1.0
profiles_sample_rate=1.0

def sentry_init():
    try:
        sentry_sdk.init(
            dsn=dsn,
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            traces_sample_rate=traces_sample_rate,
            profiles_sample_rate=profiles_sample_rate
        )
    except Exception as error:
        print('error in utils/sentry.py/sentry_init()', error)
        sentry_sdk.capture_exception(error)
        sentry_sdk.flush()
        raise error