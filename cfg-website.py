class Webpage:
    def __init__(self, suffix, options, back):
        self.suffix = suffix
        self.options = options
        self.back = back

    def page_link(self):
        return f"https://codefirstgirls.com{self.suffix}"

    def output_message(self):
        print(f"You are currently on the URL: {self.page_link()}")
        return input(f"Where are you clicking?\nOptions: {self.options}\n").title().strip()


homepage = Webpage("/", "Courses, Opportunities", "homepage")
courses = Webpage("/courses", "CFG Degree, Back", "homepage")
cfg_degree = Webpage("/cfgdegree/", "Back", "courses")
opportunities = Webpage("/opportunities", "Ambassador, Back", "homepage")
ambassador = Webpage("/ambassador/", "Back", "opportunities")


from collections import deque


def cfg_website(current_page, website_stack=deque()):
    user_input = current_page.output_message()
    while True:
        website_stack.append(current_page)
        print(website_stack)
        if user_input == "Homepage":
            current_page = homepage
        if user_input == "Courses":
            current_page = courses
        if user_input == "Cfg Degree":
            current_page = cfg_degree
        if user_input == "Opportunities":
            current_page = opportunities
        if user_input == "Ambassador":
            current_page = ambassador
        if user_input == "Back":
            website_stack.pop()
            current_page = website_stack[-1]
        cfg_website(current_page)
        return


cfg_website(homepage)
