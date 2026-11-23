# update_tool_labels.ps1
# Script to update tool_label fields in CEAMSTools JSON files to match the updated naming convention
# WARNING : the script was changing the JSON file format, so only the updates was used to update tools name.

$basePath = "c:\Users\klacourse\Documents\snooz_workspace\snooz-package-ceams\tools\CEAMSTools"

# Define the mapping of tool names to their new labels
$updates = @{
    "DetectArtifacts" = "Detect EEG Artifacts"
    "DetectREMsYASA" = "Detect REM events with YASA"
    "EditAnnotations" = "Edit Snooz Annotations"
    "ExtractAnnotation" = "Extract Snooz Annotations"
    "ImportSleepStagesVector" = "Import Sleep Stage Text Vector"
    "ScoreSleepStagesYASA" = "Score Sleep Stages with YASA"
    "ValidateSnoozTSVFile" = "Validate Snooz Annotation File"
    "PowerSpectralAnalysis" = "Analyze EEG Spectral Power"
    "SlowWaveDetection" = "Detect Slow Waves"
    "SpindleDetectionA7" = "Detect Spindles with A7"
    "SpindleDetectionMartin" = "Detect Spindles with Martin"
    "SpindleDetectionSumo" = "Detect Spindles with SUMO"
    "OxygenSaturationReport" = "Report Oxygen Saturation"
    "SleepBouts" = "Report Sleep Bouts"
    "SleepCycleExport" = "Report Sleep Cycle"
    "SleepReport" = "Report Sleep Variables"
    "SlowWaveClassification" = "Classify Slow Waves"
    "CompareEventsFromPSG" = "Evaluate Detected Events"
    "PSACohortReview" = "Review EEG Spectral Power for the cohort"
    "DetectionsCohortReview" = "Review Detections for the Cohort"
    "SlowWaveImages" = "Visualize Slow Waves"
}

Write-Host "Starting tool_label updates..." -ForegroundColor Cyan
Write-Host "Base path: $basePath`n" -ForegroundColor Yellow

$successCount = 0
$failCount = 0

# Process each tool
foreach ($toolName in $updates.Keys) {
    $filePath = Join-Path $basePath "$toolName\$toolName.json"
    
    if (Test-Path $filePath) {
        try {
            Write-Host "Processing: $toolName" -ForegroundColor White
            
            # Read the JSON file
            $content = Get-Content $filePath -Raw -Encoding UTF8
            $json = $content | ConvertFrom-Json
            
            # Store old value for comparison
            $oldLabel = $json.tool_params.tool_label
            
            # Update the tool_label
            $json.tool_params.tool_label = $updates[$toolName]
            
            # Write back to file with proper formatting
            $json | ConvertTo-Json -Depth 100 | Set-Content $filePath -Encoding UTF8
            
            Write-Host "  Old: '$oldLabel'" -ForegroundColor Gray
            Write-Host "  New: '$($updates[$toolName])'" -ForegroundColor Green
            Write-Host ""
            
            $successCount++
        }
        catch {
            Write-Host "  ERROR: Failed to update $toolName" -ForegroundColor Red
            Write-Host "  $($_.Exception.Message)" -ForegroundColor Red
            Write-Host ""
            $failCount++
        }
    }
    else {
        Write-Host "  WARNING: File not found - $filePath" -ForegroundColor Red
        Write-Host ""
        $failCount++
    }
}

# Summary
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "Update Summary:" -ForegroundColor Cyan
Write-Host "  Successfully updated: $successCount" -ForegroundColor Green
Write-Host "  Failed: $failCount" -ForegroundColor $(if ($failCount -gt 0) { "Red" } else { "Green" })
Write-Host "======================================" -ForegroundColor Cyan