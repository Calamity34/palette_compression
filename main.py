import argparse, sys, painting, cv2
import pandas as pd
from colorama import init, Style, Fore
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from time import time
from os import path
init()

if __name__ == "__main__":
    # check if fp is passed
    if not len(sys.argv) > 1:
        exit(f"{Fore.LIGHTRED_EX}ERROR: filepath is not given{Style.RESET_ALL}")

    # parse arguments
    delta = time()
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?')
    parser.add_argument('pcount', nargs='?', default='2')
    parser.add_argument('dbscan', nargs='?', default='n')
    args = parser.parse_args(sys.argv[1:])


    # validate some stuff
    if not path.exists(args.filepath):
        exit(f"{Fore.LIGHTRED_EX}ERROR: file probably doesn't exist{Style.RESET_ALL}")

    if not args.pcount.isdigit() or args.pcount == "0":
        exit(f"{Fore.LIGHTRED_EX}ERROR: pcount argument is not a positive integer{Style.RESET_ALL}")

    if args.dbscan.lower() not in ["y","yes","n","no"]:
        exit(f"{Fore.LIGHTRED_EX}ERROR: can't understand dbscan argument, available values: y, yes, n, no{Style.RESET_ALL}")

    # reshape image
    img = cv2.imread(args.filepath)
    print(f"Read file after {Fore.GREEN}{time() - delta:0.3f}s{Style.RESET_ALL}")
    x, y, z = img.shape
    X = img.reshape((x*y, z))

    # KMeans
    if args.dbscan.lower() in ["n","no"]:
        KM_model = KMeans(n_clusters=int(args.pcount))
        y_KM = KM_model.fit_predict(X)
        print(f"Model trained after {Fore.GREEN}{time() - delta:0.3f}s{Style.RESET_ALL}")
        new_img = painting.fill_color(X, y_KM).reshape((x, y, z))
        print(f"Colors averaged out after {Fore.GREEN}{time() - delta:0.3f}s{Style.RESET_ALL}")
        dot_ind = args.filepath.rfind(".")
        new_filename = args.filepath[:dot_ind] + "_kmeans_" + args.pcount + args.filepath[dot_ind:]
        painting.draw_picture(new_img, save=True, filename=new_filename)
    # DBSCAN
    elif args.dbscan.lower() in ["y","yes"]:
        DB_model = DBSCAN(n_jobs=-1)
        y_DB = DB_model.fit_predict(X)
        print(f"Model trained after {Fore.GREEN}{time() - delta:0.3f}s{Style.RESET_ALL}")
        # k = pd.Series(y_DB).nunique()
        # print(f"Count of clusters is {k}")
        new_img = painting.fill_color(X, y_DB, dbscan=True).reshape((x, y, z))
        print(f"Colors averaged out after {Fore.GREEN}{time() - delta:0.3f}s{Style.RESET_ALL}")
        dot_ind = args.filepath.rfind(".")
        new_filename = args.filepath[:dot_ind] + "_dbscan_" + args.pcount + args.filepath[dot_ind:]
        painting.draw_picture(new_img, save=True, filename=new_filename)

    # show results
    print(f"Done in {Style.BRIGHT}{Fore.GREEN}{time() - delta:0.3f}s{Style.RESET_ALL}\n")
    oldsize = path.getsize(args.filepath)
    newsize = path.getsize(new_filename)
    print(f"Saved as  : {Fore.LIGHTBLUE_EX}{new_filename}{Style.RESET_ALL}")
    print(f"File size : {Fore.LIGHTRED_EX}{oldsize:,d}{Style.RESET_ALL} -> {Fore.LIGHTGREEN_EX}{newsize:,d}{Style.RESET_ALL} bytes")
    print(f"Difference: {Fore.LIGHTBLUE_EX}{(newsize/oldsize*100):0.2f}%{Style.RESET_ALL} of original")
