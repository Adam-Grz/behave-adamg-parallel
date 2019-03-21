import os
from distutils.dir_util import copy_tree
from time import gmtime, strftime
import re
from utils.matplotlib import (steps_chart,
							  scens_chart,
							  feats_chart)

datetime = strftime("%Y-%m-%d %H:%M:%S", gmtime()).replace("-","_").replace(":","_")

def reporter():
	# copy files and folders from '/html' to '/TestReports/[date and time after test run]'
	fromDirectory = "html"
	toDirectory = f"TestReports/{datetime}"
	copy_tree(fromDirectory, toDirectory)

	# get a list of files from 'reports' folder
	report_files = os.listdir("./reports")
	
	counter = 1
	green_steps = 0
	blue_steps = 0
	red_steps = 0
	green_steps_for_scenario = 0
	blue_steps_for_scenario = 0
	red_steps_for_scenario = 0
	green_scenarios = 0
	blue_scenarios = 0
	red_scenarios = 0
	is_steps_chart = False
	is_scens_chart = False
	is_feats_chart = False
	red_fs = 0
	blue_fs = 0
	green_fs = 0

	for file in report_files:
		with open(f"{toDirectory}/index.html", 'r') as rl:
			dst_lines = rl.readlines()

		with open(f"reports/{file}", 'r') as src:
			with open(f"{toDirectory}/index.html", 'w') as dst:
				# Getting the feature name
				name_tag = re.findall(r"features.+?\"", src.readline())
				feature_title = name_tag[0].split(".")[-1].replace("\"", "")

				# Putting each scenario name and steps into a multidimensional list
				src_dump = src.readlines()
				no_scens = sum("Scenario:" in s for s in src_dump)
				src_good = [[] for x in range(no_scens)]
				for a in range(0, no_scens):
					for i in range(0, len(src_dump)):
						if "@scenario.end" in src_dump[i]:
							src_temp = src_dump[:i+1]
							for b in range(0,i+1):
								src_dump[b] = "a"
							for index, c in enumerate(src_temp):
								if "Scenario" in c:
									start = index
								if "@scenario.end" in c:
									end = index - 1
							src_good[a] = src_temp[start:end]
							break

				# Enter this data in the html
				final_details = ""
				for a in range(0,len(src_good)):
					mark_scenario = ""
					green_steps_scen = 0
					blue_steps_scen = 0
					red_steps_scen = 0
					red_features = 0
					blue_features = 0
					green_features = 0
					scen_details = f"""
<tr><td style=\"background-color:lightyellow\" width=\"85%\" align=\"center\"><i><b><h4>{src_good[a][0]}</i></b></h4></td>
<!-- SCENARIO RESULT --><td></td></tr>
									"""
					for e in range(1, len(src_good[a])):
						# Gather steps results for the pie chart
						if "passed" in src_good[a][e].split("...")[1]:
							var = "style=\"background-color:lightgreen\""
							green_steps += 1
							green_steps_scen += 1
						elif "failed" in src_good[a][e].split("...")[1]:
							var = "style=\"background-color:coral\""
							red_steps += 1
							red_steps_scen += 1
						elif "skipped" in src_good[a][e].split("...")[1]:
							var = "style=\"background-color:lightblue\""
							blue_steps += 1
							blue_steps_scen += 1
						scen_details = scen_details + f"""
<tr>
  <td><h5>{src_good[a][e].split("...")[0]}</h5></td>
  <td {var}>{src_good[a][e].split("...")[1].split("in")[0]}</td>
</tr>"""

					# Gather scenarios results for the pie chart
					if red_steps_scen > 0:
						red_scenarios += 1
						mark_scenario = "style=\"background-color:red\""
					elif blue_steps_scen > 0 and red_steps == 0:
						blue_scenarios += 1
						mark_scenario = "style=\"background-color:blue\""
					elif green_steps_scen > 0:
						green_scenarios += 1
						mark_scenario = "style=\"background-color:green\""

					# Gather feature results for the pie chart
					if red_scenarios > 0:
						red_features += 1
					if blue_scenarios > 0 and red_scenarios == 0:
						blue_features += 1
					if green_scenarios > 0 and blue_scenarios == 0 and red_scenarios == 0:
						green_features += 1

					steps_chart(green_steps, blue_steps, red_steps, f"TestReports/{datetime}")
					scens_chart(green_scenarios, blue_scenarios, red_scenarios, f"TestReports/{datetime}")
					final_details = final_details + scen_details

					# Marking scenarios as pass/skip/fail
					aa = final_details.split("\n")
					
					for line in range(0,len(aa)):
						if "<!-- SCENARIO RESULT --><td></td></tr>" in aa[line]:
							aa[line] = f"<!-- SCENARIO RESULT --><td width=\"15%\" {mark_scenario}></td></tr>"
					
					final_details = "\n".join(aa)

				if red_features > 0:
					red_fs += 1
				if blue_features > 0:
					blue_fs += 1
				if green_features > 0:
					green_fs += 1

				feats_chart(green_fs, blue_fs, red_fs, f"TestReports/{datetime}")

				for line in dst_lines:
					# Top banner
					if "<h1>Test run</h1>" in line:
						line = f"<h1>Test run - {strftime('%Y-%m-%d %H:%M:%S', gmtime())}</h1>"
					# Insert charts
					if "<td style=\"width:33%\" chart=\"steps\">" in line and not is_steps_chart:
						line = f"""<td style=\"width:33%\" chart=\"steps\">
						<img src=\"{os.getcwd()}/TestReports/{datetime}/images/steps_chart.png\" style=\"width:300px;height:225px;\">"""
						is_steps_chart = True
					if "<td style=\"width:33%\" chart=\"scenarios\">" in line and not is_scens_chart:
						line = f"""<td style=\"width:33%\" chart=\"scenarios\">
						<img src=\"{os.getcwd()}/TestReports/{datetime}/images/scens_chart.png\" style=\"width:300px;height:225px;\">"""
						is_scens_chart = True
					if "<td style=\"width:33%\" chart=\"features\">" in line and not is_feats_chart:
						line = f"""<td style=\"width:33%\" chart=\"scenarios\">
						<img src=\"{os.getcwd()}/TestReports/{datetime}/images/feats_chart.png\" style=\"width:300px;height:225px;\">"""
						is_feats_chart = True
					# Menu items
					if "features_menu" in line:
						line = line + f"\n<a href=\"#{str(counter)}\">Feature: {feature_title}</a><br>"
					# Main body, results details
					if "testrun_details" in line:
						line = line + f"""   
										<table width="100%">     
										<hr>
								        <h3 id="{str(counter)}">Feature: {feature_title}</h3><h5><a href=\"#menu\">  |  back to Menu</a></h5>
								        {final_details}
								        </table>
								        """
					dst.write(line)
		counter += 1
	with open('foldername.txt', 'w') as ff:
		ff.write(f'TestReports/{datetime}')

reporter()