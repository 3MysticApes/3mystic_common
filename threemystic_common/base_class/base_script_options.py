import sys, getopt, json, argparse, inspect
from typing import final
from pathlib import Path  

class base_process_options:
    def __init__(self, common, argparse_parser = None):
        self.argparse_parser = argparse_parser
        
        self._common = common
        self.this = base_process_options
        self.processed_options_as_dictionary = {}
        self.__argKeys = {}
        return
    
    def get_arg_keys(self):
        return self.__argKeys

    def add_arg_keys(self, arg_keys):
        self._common.helper_type().dictionary().merge_dictionary(self.__argKeys, arg_keys)

    def get_parser(self, parser = None):
        if parser is not None:
            return parser
        
        if self.argparse_parser is not None:
            return self.argparse_parser
        
        self.argparse_parser = argparse.ArgumentParser()
        return self.get_parser(parser= self.argparse_parser)

    def print_help(self, *argparse_data, argparse_parser = None):
        main_dictionary = {}
        for item in argparse_data:
            for arg_values in item:
                self._common.helper_type().dictionary().merge_dictionary(main_dictionary, arg_values)

        parser = self.get_parser(parser= argparse_parser)
        for (arg, data) in main_dictionary.items():
            parser.add_argument(arg, **data)
        
        parser.print_help()
        

    def _process_opts_getopt(self, class_object, argv, argKeys):
        
        try:
            opts, arg = getopt.getopt(argv,'hv',argKeys.keys())
        except getopt.GetoptError as err:
            print(str(err))
            raise

        for opt, arg in opts:
            attrName = opt.lstrip("-").rstrip("=").replace("-", "_")
            if opt in ('-h', '--help'):
                if self._common.helper_type().general().is_type(class_object, dict):
                    class_object["help"] = True
                    continue
                if hasattr(class_object, "help"):
                    setattr(class_object, "help", True)
                continue;
            elif not hasattr(class_object, attrName) and not self._common.helper_type().general().is_type(class_object, dict):
                continue
    
            
            keyname = opt.lstrip("-")
            if not keyname in argKeys:
                keyname += '='

            customDataSet = argKeys[keyname][len(argKeys[keyname])-1]
            if not customDataSet is None:
                if self._common.helper_type().general().is_type(class_object, dict):                    
                    class_object[attrName] = customDataSet(arg)
                    continue
                setattr(class_object, attrName, customDataSet(arg))
                continue
            
            if self._common.helper_type().general().is_type(class_object, dict):                    
                class_object[attrName] = arg
                continue

            setattr(class_object, attrName, arg)

    def _process_opts(self, argv, argKeys, store_as_dict = False, parser = None):
        parser = self.get_parser(parser= parser)

        default_verbose = {
            "default": False, 
            "help": "Verbose output",
            "dest": "output_verbose",
            "action": 'store_true'
        }
        

        for (arg, data) in argKeys.items():
            flags = self._common.split_string(arg)
            parser.add_argument(*flags, **data)



        if not store_as_dict:
            _, extra = parser.parse_known_args(argv, namespace= self)
        else:
            processed_data, extra = parser.parse_known_args(argv)
            self.processed_options_as_dictionary = vars(processed_data)
        
        return extra
