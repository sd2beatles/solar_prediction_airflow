from configparser import ConfigParser
import os

def get_value(path,key,value,interpolation=True):
    # if you want to avoid interpolation,set interpolation as False
    parser=ConfigParser() if interpolation else ConfigParser(interpolation=None)
    
    parser.read(path)
    return parser.get(key,value)