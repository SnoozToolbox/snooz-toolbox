"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

Memory Management utilities for Snooz application.
Provides cross-platform memory cleanup and virtual memory release.
"""
import gc
import os
import platform

from Managers.Manager import Manager
import config


class MemoryManager(Manager):
    """
    Cross-platform memory management for Snooz.
    
    Provides utilities to clean up memory usage and release virtual memory
    back to the operating system. Simplified version without monitoring.
    """
    
    def __init__(self, managers):
        super().__init__(managers)
        
    def initialize(self):
        """Initialize the memory manager."""
        pass
    
    def light_cleanup(self):
        """
        Perform light memory cleanup without affecting user experience.
        Safe to call during normal operation.
        """
        # Just do a gentle garbage collection
        gc.collect()
    
    def aggressive_cleanup(self):
        """
        Perform aggressive memory cleanup.
        Should only be called during app shutdown or when user explicitly requests it.
        """
        if hasattr(self._managers, 'package_manager'):
            self._managers.package_manager.cleanup_for_shutdown()
        else:
            # Fallback if package manager not available
            self._force_memory_release()
    
    def _force_memory_release(self):
        """
        Force memory release using platform-specific techniques.
        """
        # Multiple garbage collection cycles
        for _ in range(3):
            gc.collect()
        
        try:
            if platform.system() == "Windows":
                self._windows_memory_release()
            elif platform.system() == "Darwin":  # macOS
                self._macos_memory_release()
            elif platform.system() == "Linux":
                self._linux_memory_release()
        except Exception:
            pass
    
    def _windows_memory_release(self):
        """Windows-specific memory release."""
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            current_process = kernel32.GetCurrentProcess()
            
            # Empty working set
            kernel32.SetProcessWorkingSetSize(current_process, -1, -1)
            kernel32.EmptyWorkingSet(current_process)
            
        except Exception:
            pass
    
    def _macos_memory_release(self):
        """macOS-specific memory release."""
        try:
            import ctypes
            import ctypes.util
            
            libc_path = ctypes.util.find_library("c")
            if libc_path:
                libc = ctypes.CDLL(libc_path)
                
                if hasattr(libc, 'malloc_zone_pressure_relief'):
                    libc.malloc_zone_pressure_relief(None, 0)
                    
        except Exception:
            pass
    
    def _linux_memory_release(self):
        """Linux-specific memory release."""
        try:
            import ctypes
            import ctypes.util
            
            libc_path = ctypes.util.find_library("c")
            if libc_path:
                libc = ctypes.CDLL(libc_path)
                
                if hasattr(libc, 'malloc_trim'):
                    libc.malloc_trim(0)
                    
        except Exception:
            pass
    
    def log_memory_stats(self, label=""):
        """
        Log current memory statistics.
        
        Parameters
        ----------
        label : str
            Optional label for the log entry
        """
        memory_info = self.get_memory_info()
        if memory_info:
            rss_mb = memory_info['rss'] / 1024 / 1024
            vms_mb = memory_info['vms'] / 1024 / 1024
            
            message = f"Memory {label}: RSS={rss_mb:.1f}MB, VMS={vms_mb:.1f}MB, {memory_info['percent']:.1f}%"
            
            if hasattr(self._managers, 'log_manager'):
                self._managers.log_manager.add_log("MemoryManager", message)
            else:
                print(message)
