from behave import then
from shortcuts.ECs.ecs import (presenceID,
	                           presenceXP,
	                           visibilityXP,
	                           visibilityID)
from shortcuts.finds.singular import (findID,
	                                  findXP)
from shortcuts.finds.plural import (findIDs,
	                                  findXPs)


@then("The page titled \"{title}\" has loaded")
def page_titled_title_has_loaded(context, title):
    presenceXP(context, "//head/title")
    page_title = findXP(context, "//head/title").get_attribute("innerHTML")
    context.test_output.write(f"{page_title}\n")
    context.test_output.write(f"{title}\n")
    assert title in page_title