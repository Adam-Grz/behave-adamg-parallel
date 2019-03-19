This will generate an HTML report from the behave's reports.

At the moment the test suite is run using runner[browser].py, which renames [browser].ini to behave.ini. behave.ini has set:
junit = true
format = plain
which outputs an .xml in /reports folder.

This script then grabs the .xml files from the /reports folder and creates an HTML report under TestReports/[datetime]/ using a free template I found online at http://www.htmltemplates.net

I am not a programmer, and this script is terribly written. Hold your hate, I don't care. It does what I want it to.
