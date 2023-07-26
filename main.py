from subprocess import Popen

from server import initialise
from server.helpers import normalise_path


def main():
    """
    Summary
    -------
    exhaust the initialise generator and run the server
    """
    try:
        with Popen(['code', '--install-extension', normalise_path('out/wingman.vsix')]) as _:
            pass

        for _ in initialise():
            pass

    finally:
        with Popen(['code', '--uninstall-extension', 'undefined_publisher.wingman']) as process:
            process.wait()


if __name__ == '__main__':
    main()
