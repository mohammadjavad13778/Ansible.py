#!/bin/bash

# Script options
delete_files=0

# Validate inputs
read -p "Enter project directory: " project_directory
if [ -z "$project_directory" ]; then
  echo "Error: No directory entered" >&2
  exit 1
fi 

if [ ! -d "$project_directory" ]; then
  echo "Error: $project_directory is not a valid directory" >&2
  exit 1 
fi

# Parse options
while getopts ":hd" opt; do
  case $opt in
    h)  
      echo "Usage: $0 [-d] <project_dir>" >&2
      exit 0
      ;;
    
    d)
      delete_files=1
      ;;

    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done  

# Main logic
main() {

  if [ "$delete_files" -eq 1 ]; then 
    echo "Deleting files in $project_directory"
    rm $project_directory/* > /dev/null 2>&1
  fi

  echo "Executing script 1"
  python3 ./Ansible.py $project_directory

  echo "Executing script 2" 
  python3 ./README.py $project_directory

}

# Run main 
main

echo "Script Completed ! The Ansible Playbook and README files have been generated !"