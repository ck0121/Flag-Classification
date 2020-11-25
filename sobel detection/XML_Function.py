import xml.dom.minidom

def GenerateXML(filename):
    global a
    a = []
    # 在内存中创建一个空的文档
    doc = xml.dom.minidom.Document()
    # 创建一个根节点Managers对象
    root = doc.createElement('annotation')

    # 将根节点添加到文档对象中
    doc.appendChild(root)

    # 根节点Annotation和子节点Folder,Filename,path
    nodeFolder = doc.createElement("folder")
    nodeFolder.appendChild(doc.createTextNode("Folder Name"))
    nodeFilename = doc.createElement("filename")
    nodeFilename.appendChild(doc.createTextNode("File Name"))
    nodePath = doc.createElement("path")
    nodePath.appendChild(doc.createTextNode("Path"))

    # 父节点Size和子节点Width,Height
    nodeSize = doc.createElement("Size")
    nodeWidth = doc.createElement("Width")
    nodeWidth.appendChild(doc.createTextNode('400'))
    nodeHeight = doc.createElement("Height")
    nodeHeight.appendChild(doc.createTextNode('300'))

    # 父节点Object和子节点Name(label),Bndbox
    nodeObject = doc.createElement("object")
    nodeName = doc.createElement("name")
    nodeName.appendChild(doc.createTextNode('label'))

    # 父节点Bndbox和子节点Xmin,Ymin,Xmax,Ymax
    nodeBndbox = doc.createElement("bndbox")
    nodeXmin = doc.createElement("xmin")
    nodeXmin.appendChild(doc.createTextNode(str(a)))
    nodeYmin = doc.createElement("xmin")
    nodeYmin.appendChild(doc.createTextNode(str(a)))
    nodeXmax = doc.createElement("xmin")
    nodeXmax.appendChild(doc.createTextNode(str(a)))
    nodeYmax = doc.createElement("xmin")
    nodeYmax.appendChild(doc.createTextNode(str(a)))

    # 将子节点添加到父节点下
    nodeSize.appendChild(nodeWidth)
    nodeSize.appendChild(nodeHeight)

    nodeObject.appendChild(nodeName)
    nodeObject.appendChild(nodeBndbox)

    nodeBndbox.appendChild(nodeXmin)
    nodeBndbox.appendChild(nodeYmin)
    nodeBndbox.appendChild(nodeXmax)
    nodeBndbox.appendChild(nodeYmax)

    # 将父节点添加到根节点下
    root.appendChild(nodeFolder)
    root.appendChild(nodeFilename)
    root.appendChild(nodePath)
    root.appendChild(nodeSize)
    root.appendChild(nodeObject)


    # 开始写xml文档
    fp = open(filename, 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")

if __name__=="__main__":
    GenerateXML(r'D:\Blander Flag\Flag-Classification\sobel detection\Resources\Xml12.xml')