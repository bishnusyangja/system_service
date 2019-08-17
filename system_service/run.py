import argparse

from system_service import app

if __name__ == '__main__':
    run_parser = argparse.ArgumentParser(add_help=False)

    run_parser.add_argument('--reload', dest="reload", action="store_true")
    run_parser.add_argument('--no-reload', dest="reload", action="store_false")
    run_parser.set_defaults(reload=False)

    run_parser.add_argument('--host')
    run_parser.add_argument('--port')

    run_args = run_parser.parse_args()

    app.run(
        run_args.host,
        run_args.port,
        use_reloader=run_args.reload)
