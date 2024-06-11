import sys

from show_job.utils import get_logger

logger = get_logger(__name__)


def main():
    if len(sys.argv) > 1:
        job_name = sys.argv[1]
        logger.info(f"Showing details for job: {job_name}")
    else:
        logger.info("No job specified. Usage: show-job <job_name>")


if __name__ == "__main__":
    main()
