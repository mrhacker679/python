`import shutil `

 Copy a file from source to destination
`shutil.copy(source, destination)`

 Copy a file from source to destination preserving metadata
`shutil.copy2(source, destination)`

 Copy a file or directory recursively from source to destination
`shutil.copytree(source, destination)`

 Remove a file or directory
`shutil.rmtree(path)`

 Move a file or directory from source to destination (or to rename)
`shutil.move(source, destination)`

 Create a zip archive of a file or directory
`shutil.make_archive(base_name, format, root_dir)`

 Extract the contents of a zip archive to a directory
`shutil.unpack_archive(filename, extract_dir)`

 Get information about a file or directory
`shutil.disk_usage(path)`
