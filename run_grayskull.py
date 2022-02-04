"""Touch up the conda recipe from grayskull using conda-souschef."""
from souschef.recipe import Recipe
import os
from os.path import join
from pathlib import Path
from shutil import copyfile
import composition_based_feature_vector as module

name, version = module.__name__, module.__version__
os.system(f"grayskull pypi {name}=={version}")

Path("scratch").mkdir(exist_ok=True)

fpath = join(name, "meta.yaml")
fpath2 = join("scratch", "meta.yaml")
my_recipe = Recipe(load_file=fpath)
my_recipe["requirements"]["host"].append("flit")
my_recipe["build"].add_section("noarch")
my_recipe["build"]["noarch"] = "python"
my_recipe.save(fpath)
my_recipe.save(fpath2)

copyfile("LICENSE", join("scratch", "LICENSE"))
