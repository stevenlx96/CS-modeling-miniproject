import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('TypeCheck')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class TypeCheck(PluginBase):
    def main(self):

        active_node = self.active_node
        core = self.core
        logger = self.logger
        META = self.META
 
        nodes = core.load_sub_tree(active_node)
        places = []
        transactions = []
        arcsrcs = []
        arcdsts = []
    
        for node in nodes:
            if core.is_instance_of(node,META['Place']):
                places.append(core.get_path(node))
            if core.is_instance_of(node,META['Transaction']):
                transactions.append(core.get_path(node))
            if core.is_instance_of(node, META['Arc']):
                arcsrcs.append(core.get_pointer_path(node, 'src'))
                arcdsts.append(core.get_pointer_path(node, 'dst'))


        placesrcs = []
        transrcs = []
        placedsts = []
        trandsts = []
        for src in arcsrcs:
            if src in places:
                placesrcs.append(src)
            if src in transactions:
                transrcs.append(src)
        for dst in arcdsts:
            if dst in places:
                placedsts.append(dst)
            if dst in transactions:
                trandsts.append(dst)
    
        trandup = False
        placedup = False
        if len(trandsts) > len(set(trandsts)) or len(transrcs) > len(set(transrcs)):
            trandup = True
        if len(placesrcs) > len(set(placesrcs)) or len(placedsts) > len(set(placedsts)):
            placedup = True

        if trandup == False and placedup == False:
            self.send_notification('You have a Workflow')
        elif trandup == True and placedup == False:
            self.send_notification('Your have a Marked graph')
        elif trandup == False and placedup == True:
            self.send_notification('Your have a State machine')
        else:
            self.send_notification('Your have a Free-choice petri net')
