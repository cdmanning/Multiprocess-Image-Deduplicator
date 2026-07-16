@echo off
title Multiprocess Image Deduplicator

echo.
echo [PROCESS] Starting duplicate image scan...
echo -------------------------------------------------------
echo.

python multiprocess_image_deduplicator.py

echo.
echo -------------------------------------------------------
echo [FINISHED] Process complete.
echo.
pause