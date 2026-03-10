"""Shared helpers for stable joblib parallel execution in Snooz modules."""

import os
import sys


def select_joblib_backend(env_var="CEAMS_JOBLIB_BACKEND"):
    """
    Return a safe joblib backend for the current runtime.

    Rules:
    - Respect env override when valid: loky|threading|multiprocessing.
    - In frozen executables, default to threading for better stability.
    - Otherwise default to loky for source execution.
    """
    valid_backends = {"loky", "threading", "multiprocessing"}
    backend_override = os.environ.get(env_var)
    if backend_override in valid_backends:
        return backend_override

    if getattr(sys, "frozen", False):
        return "threading"

    return "loky"


def normalize_n_jobs(n_jobs, task_count):
    """Normalize n_jobs to an integer in [1, min(cpu_count, task_count)]."""
    if task_count <= 1:
        return 1

    max_workers = min(os.cpu_count() or 1, task_count)

    if n_jobs is None or n_jobs == 0 or n_jobs < -1:
        return 1
    if n_jobs == -1:
        return max_workers

    return max(1, min(int(n_jobs), max_workers))
