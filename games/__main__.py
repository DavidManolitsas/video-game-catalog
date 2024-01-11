import argparse
from games.util.template_util import get_template
from games.api.open_critic_service import OpenCriticService


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    # open critic api key
    arg_parser.add_argument("-k", "--key", type=str)
    args = arg_parser.parse_args()

    service = OpenCriticService(app_key=args.key)
    releases = service.get_upcoming_releases()
    recent = service.get_recently_released_games()

    template = get_template(file_name="index.html.jinja2")
    with open(f"app/index.html", "w", encoding="UTF-8") as file:
        file.write(
            template.render(
                games=releases,
                recent=recent
            )
        )
