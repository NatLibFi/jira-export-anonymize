#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 *
 * Jira issue export anonymizer
 *
 * Copyright (C) 2018 University Of Helsinki (The National Library Of Finland)
 *
 * This file is part of jira-export-anonymize
 *
 * jira-export-anonymize  is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * jira-export-anonymize is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
'''

import sys
from uuid import uuid4 as uuid
from lxml import etree

if len(sys.argv) < 2:
    print 'Filename needed as an argument'
    sys.exit(1)

for event, element in etree.iterparse(sys.argv[1]):
        if (element.tag in ('assignee', 'reporter')):
            element.set('username', str(uuid()))
            element.text = ''
        elif element.tag == 'comment':
            element.set('author', str(uuid()))

        print(etree.tostring(element))
