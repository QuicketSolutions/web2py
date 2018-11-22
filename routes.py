default_application = "Quicket"

routes_app = (
    (r"/(?P<app>admin|app)\b.*", r"\g<app>"),
    (
        r"/(?P<app>arms_test|northlake_old|peoria_test|lemont_test|champaign_test|payticket)\b.*",
        r"\g<app>",
    ),
)

routes_in = [
    # make sure you do not break admin
    ("/admin", "/admin"),
    ("/admin/$anything", "/admin/$anything"),
    # make sure you do not break appadmin
    ("/$app/appadmin", "/$app/appadmin"),
    ("/$app/appadmin/$anything", "/$app/appadmin/$anything"),
    ("/static/$anything", "/oneapp/static/$anything"),
    ("/$domain/v2/nonlocal$anything", "/oneapp/v2/non_local$anything?client=$domain"),
    ("/$domain/v2_1/nonlocal$anything", "/oneapp/v2_1/non_local$anything?client=$domain"),
    ("/$domain(?P<rest>.*)$", "/oneapp\g<rest>?client=$domain"),
]

routes_out = [(a, b) for (b, a) in routes_in]

logging = "debug"
