import os


project_folder = "/opt/projects/nesy/NESY.Courier.Mobile"


control = """
            buildConfigField "String", "BASE_URL", '"https://nesy-arasdx-dev-api.araskargo.com.tr/"'
            buildConfigField "String", "BASE_URL_HOST", '"nesy-arasdx-dev-api.araskargo.com.tr"'
"""
change = f"""
            buildConfigField "String", "BASE_URL", '"http://10.0.2.2:8080/"'
            buildConfigField "String", "BASE_URL_HOST", '"10.0.2.2:8080"'
"""

buildFile = os.path.join(project_folder, "app", "build.gradle")
buildFileCodes = ""
with open(buildFile, "r") as gradle:
    buildFileCodes = gradle.read()

buildFileCodes = buildFileCodes.replace(control, change)

with open(buildFile, "w") as gradle:
    gradle.write(buildFileCodes)
