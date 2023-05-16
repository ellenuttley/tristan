class Webpage:
    def __init__(self, suffix, options):
        self.suffix = suffix
        self.options = options

    def page_link(self):
        return f"https://codefirstgirls.com{self.suffix}"

    def output_message(self):
        print(f"You are currently on the URL: {self.page_link()}")
        return input(f"Where are you clicking?\nOptions: {self.options}\n").title().strip()


class Homepage(Webpage):
    def __init__(self):
        suffix = "/"
        options = "Courses, Opportunities"
        super().__init__(suffix, options)


class CoursesPage(Webpage):
    def __init__(self):
        suffix = "/courses"
        options = "CFG Degree, Back"
        super().__init__(suffix, options)

    def back(self):
        Homepage().output_message()


class CfgDegreePage(CoursesPage):
    def __init__(self):
        suffix = "/cfgdegree/"
        super().__init__()
        self.suffix += suffix

    def page_options(self):
        return "Back"

    def back(self):
        CoursesPage().output_message()


class OpportunitiesPage(Webpage):
    def __init__(self):
        suffix = "/opportunities"
        options = "Ambassador, Back"
        super().__init__(suffix, options)

    def back(self):
        Homepage().output_message()

class AmbassadorPage(OpportunitiesPage):
    def __init__(self):
        name = "Ambassador"
        suffix = "/ambassador"
        super().__init__()
        self.suffix += suffix

    def page_options(self):
        return "Back"

    def back(self):
        OpportunitiesPage().output_message()


homepage = Homepage()
courses = CoursesPage()
cfg_degree = CfgDegreePage()
opportunities = OpportunitiesPage()
ambassador = AmbassadorPage()


# @Navigator
def cfg_website(current_page):
    user_input = current_page.output_message()
    while True:
        if user_input == "Homepage":
            current_page = Homepage()
        if user_input == "Courses":
            current_page = CoursesPage()
        if user_input == "Cfg Degree":
            current_page = CfgDegreePage()
        if user_input == "Opportunities":
            current_page = OpportunitiesPage()
        if user_input == "Ambassador":
            current_page = AmbassadorPage()
        if user_input == "Back":
            current_page.back()
        cfg_website(current_page)
        return


cfg_website(Homepage())
