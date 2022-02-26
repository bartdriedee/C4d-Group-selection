import c4d
# Welcome to the world of Python


# Script state in the menu or the command palette
# Return True or c4d.CMD_ENABLED to enable, False or 0 to disable
# Alternatively return c4d.CMD_ENABLED|c4d.CMD_VALUE to enable and check/mark
#def state():
#    return True

class InsertNull():
    def __init__(self, name = 'inserting Null'):
        print (name)

    def main(self, relative=True):
        doc = c4d.documents.GetActiveDocument()
        doc.StartUndo()
        selection = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN | c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER )

        new_group = self.createGroup('null')
        doc.InsertObject(new_group)

        if selection:
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, selection[0])
            parent = selection[0].GetUp()

            if parent:
                new_group.InsertUnder(parent)
            for obj in selection:
                doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
                obj.InsertUnder(new_group) #insert the child under the parent
            if relative:
                avg_position = self.getAvaragePosition(selection)
                new_group.SetAbsPos(avg_position)
                for obj in selection:
                    obj.SetAbsPos(obj.GetAbsPos()-avg_position)

        doc.AddUndo(c4d.UNDOTYPE_NEW, new_group)
        doc.EndUndo()
        c4d.EventAdd()

    def getAvaragePosition(self, objects):
        cumulative_position = c4d.Vector(0,0,0)
        for obj in objects:
            cumulative_position += obj.GetAbsPos()
        return cumulative_position / len(objects)

    def createGroup(self, name):
        grp_obj = c4d.BaseObject(c4d.Osplinestar)
        grp_obj[c4d.PRIM_STAR_IRAD]=0
        grp_obj[c4d.PRIM_STAR_ORAD]=0
        grp_obj[c4d.PRIM_STAR_POINTS]=3
        grp_obj[c4d.SPLINEOBJECT_INTERPOLATION]=0
        grp_obj[c4d.ID_BASELIST_NAME]=name
        return grp_obj