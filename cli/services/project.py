from cli.core.paths import exists

def validate():
    return {
        "build.gradle.kts": exists("build.gradle.kts"),
        "app": exists("app"),
        "AndroidManifest.xml": exists("app","src","main","AndroidManifest.xml")
    }
