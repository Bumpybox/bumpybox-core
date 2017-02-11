import sys


def main():

    job_status = sys.argv[0]
    job = sys.argv[1]

    import ftrack
    task = ftrack.Task(job.GetJobEnvironmentKeyValue("FTRACK_TASKID"))

    status_mapping = {
        "OnJobSubmitted": "Processing Queued",
        "OnJobStarted": "Processing",
        "OnJobFinished": "Processing Done",
        "OnJobRequeued": "Processing Queued",
        "OnJobFailed": "Processing Failed",
        "OnJobSuspended": "Processing Queued",
        "OnJobResumed": "Processing Queued",
        "OnJobPended": "Processing Queued",
        "OnJobReleased": "Processing Queued",
        "OnJobDeleted": "Processing Done",
    }

    # Fail safe for non-existing job statuses
    if job_status not in status_mapping.keys():
        return

    # Need to find the status by name
    ft_status = None
    for status in ftrack.getTaskStatuses():
        if status.getName() == status_mapping[job_status]:
            ft_status = status
            break

    task = ftrack.Task(job.GetJobEnvironmentKeyValue("FTRACK_TASKID"))
    task.setStatus(ft_status)
    print "Setting \"{0}\" to \"{1}\"".format(
        task.getName(), ft_status.getName()
    )


main()
