# Jira issue export anonymizer
Features:
- Assign a random value to comment author-attribute
- Assign a random value to assignee and reporter username-attributes and empties the text content
## Usage
```sh
pip install --user pipenv
pipenv install
pipenv run process in.xml > out.xml
```

## License and copyright

Copyright (c) 2018 **University Of Helsinki (The National Library Of Finland)**

This project's source code is licensed under the terms of **GNU Lesser General Public License Version 3** or any later version.
