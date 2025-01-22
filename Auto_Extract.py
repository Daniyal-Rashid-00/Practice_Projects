Create a Python script that monitors a specific folder for newly added `.zip` files. The script should:
1. Wait until the `.zip` file is completely downloaded by checking if the file size remains stable for 5 seconds.
2. Once stable, extract the `.zip` file into the same folder.
3. Do not delete any files after extraction.

The script should use the `watchdog` library to monitor the folder and handle events. It should also ensure that the file is fully downloaded before attempting extraction, preventing errors from incomplete downloads.
