from subprocess import Popen

from server import initialise
from server.helpers import normalise_path


def main():
    """
    Summary
    -------
    exhaust the initialise generator and run the server
    """

    with Popen(['code', '--install-extension', normalise_path('out/wingman.vsix')]) as _:
        pass

    try:
        for _ in initialise():
            pass

    finally:
        with Popen(['code', '--uninstall-extension', 'undefined_publisher.wingman']) as _:
            pass


if __name__ == '__main__':
    main()
