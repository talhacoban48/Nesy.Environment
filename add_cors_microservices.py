import os


base = os.getcwd()
project_folder = os.path.join(base, "projects", "nesy", "NESY.WebAPI")

os.chdir(project_folder)

control = "app.UseHttpsRedirection();"
change = f"""
        {control}
        app.UseCors(
            options => options.WithOrigins("http://localhost:4200").AllowAnyMethod().AllowAnyHeader().AllowAnyOrigin()
        );
"""

for api in os.listdir(project_folder):
    if api.endswith("API"):
        print(api)
        codes = ""
        Startup_path = os.path.join(api, "Startup.cs")
        if os.path.exists(Startup_path):
            with open(os.path.join(api, "Startup.cs"), "r") as Startup:
                codes = Startup.read()

            if change in codes:
                continue

            if (control in codes):
                codes = codes.replace(control, change)
                print(codes)
                with open(os.path.join(api, "Startup.cs"), "w") as Startup:
                    Startup.write(codes)



control = """
        // app.UseCors(
        //     options => options.WithOrigins("http://localhost:4200").AllowAnyMethod().AllowAnyHeader().AllowAnyOrigin()
        // );
"""
change = f"""
        app.UseCors(
            options => options.WithOrigins("http://localhost:4200").AllowAnyMethod().AllowAnyHeader().AllowAnyOrigin()
        );
"""

roleControllerStartUpFile = os.path.join(project_folder, "services", "Nesy.IdentityService.Http.Host", "Startup.cs")
roleControllerStartUpCodes = ""
with open(roleControllerStartUpFile, "r") as Startup:
    roleControllerStartUpCodes = Startup.read()

roleControllerStartUpCodes = roleControllerStartUpCodes.replace(control, change)

with open(roleControllerStartUpFile, "w") as Startup:
    Startup.write(roleControllerStartUpCodes)
