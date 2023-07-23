from server import initialise


def main():
    """
    Summary
    -------
    exhaust the initialise generator and run the server
    """
    for _ in initialise():
        pass


if __name__ == '__main__':
    main()
