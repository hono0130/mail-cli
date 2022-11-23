import click
import time

from module.output import usual_open_ratio, usual_click_ratio

@click.group()
def cli():
    pass


@cli.command()
@click.option("--open_ratio", prompt="開封率を出力しますか？[y/N]", type=bool)
@click.option("--click_ratio", prompt="反応率を出力しますか？[y/N]", type=bool)
def usual_analyze(open_ratio, click_ratio):
    if open_ratio:
        n = click.prompt("何回分の開封率を出力しますか？", type=int)
        usual_open_ratio(n, False)
        
        print("finish!")
        
    if click_ratio:
        n = click.prompt("何回分の反応率を出力しますか？", type=int)
        usual_click_ratio(n, False)

        print("finish!")


@cli.command()
@click.option("--open_attrib", prompt="属性別の開封率を出力しますか？[y/N]", type=bool)
@click.option("--click_attrib", prompt="属性別の反応率を出力しますか？[y/N]", type=bool)
def attrib_analyze(open_attrib, click_attrib):
    if open_attrib:
        pass
    if click_attrib:
        pass

@cli.command()
@click.option("--open_ratio", prompt="高い見込みの開封率を出力しますか？[y/N]", type=bool)
@click.option("--click_ratio", prompt="高い見込みの反応率を出力しますか？[y/N]", type=bool)
def high_prospects_analyze(open_ratio, click_ratio):
    if open_ratio:
        n = click.prompt("何回分の開封率を出力しますか？", type=int)
        usual_open_ratio(n, True)
        
        print("finish!")
        
    if click_ratio:
        n = click.prompt("何回分の反応率を出力しますか？", type=int)
        usual_click_ratio(n,True)

        print("finish!")


if __name__ == "__main__":
    cli()

