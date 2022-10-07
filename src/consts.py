LONG_STRING = "this is a really long string this is a really long string this is a really long string this is a really long string this is a really long string "
MEDIUM_STRING = "this is a medium string this is a medium string this is a medium string this is a medium string "
SHORT_STRING = "this is a short string"
ANOTHER_STRING = "another"

# Adding a security flaw for bandit to find
def securityRisk():
    import subprocess

    domain = input("Enter the Domain: ")
    output = subprocess.check_output(f"nslookup {domain}", shell=True, encoding="UTF-8")
    print(output)


# ADded comment 2
