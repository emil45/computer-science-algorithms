from typing import List

from utils.models import initialize_jobs
from utils.models import Job


def compatible(job: Job, jobs: List[Job]):
    """Determine if job is compatible with each job from jobs"""
    for temp_job in jobs:
        if any(time in range(temp_job.start_time, temp_job.finish_time + 1) for time in job):
            return False
    return True


def delete_jobs_that_not_compatible_with_job(requested_job: Job, jobs: List[Job]):
    return [job for job in jobs if compatible(job, [requested_job])]


def interval_scheduling_with_while_loop(jobs: List[Job]):
    accepted_jobs = []

    while jobs:
        jobs.sort(key=lambda job: job.finish_time)
        job_with_smallest_finishing_time = jobs[0]
        accepted_jobs.append(job_with_smallest_finishing_time)
        jobs = delete_jobs_that_not_compatible_with_job(job_with_smallest_finishing_time, jobs)

    return accepted_jobs


def interval_scheduling_with_for_loop(jobs: List[Job]):
    jobs.sort(key=lambda job: job.finish_time)
    accepted_jobs = []

    for job in jobs:
        if compatible(job, accepted_jobs):
            accepted_jobs.append(job)

    return accepted_jobs


if __name__ == "__main__":
    jobs = initialize_jobs()
    print(interval_scheduling_with_while_loop(jobs))
