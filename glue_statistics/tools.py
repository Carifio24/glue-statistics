from glue_statistics.icons import NOTATION_LOGO, EXPORT_LOGO, CALCULATE_LOGO, SORT_LOGO, SETTINGS_LOGO, INSTRUCTIONS_LOGO, HOME_LOGO, SAVE_LOGO, EXPAND_LOGO, COLLAPSE_LOGO, CUSTOM_COLUMN_LOGO

from glue.config import viewer_tool
from glue.viewers.common.qt.tool import Tool, SimpleToolMenu

from qtpy import QtWidgets


@viewer_tool
class AddColumnButton(Tool):
	"""
    A class used to add a column with arithmetic functionality in the viewer
    ----------
    Attributes
    ----------
    icon : str
        a formatted string that points to the icon png file location
    tool_id : str
        the id of the refresh tool used to add to toolbar
    action_text : str
        brief description of the tool's function
	tool_tip: str
		detailed tip about the tool's function
	status_tip: str
		message about tool's status
	shortcut: char
		character that can toggle the tool from keyboard
	-------
    Methods
    -------
     __init__(self,viewer):
	 	connects the StatsDataViewerviewer to the tool
	activate(self):
		action performed when tool is activated

    """

	icon = CUSTOM_COLUMN_LOGO
	tool_id = 'stats:add_column'
	action_text = 'Add Column'
	tool_tip = 'Add Column'
	status_tip = 'Add Column'

	def __init__(self, viewer):
		self.viewer = viewer

	def close(self):
		pass

	def activate(self):
		self.viewer.addColumn()



@viewer_tool
class CollapseButton(Tool):
	"""
    A class used to collapse all item in the current tree view
    ----------
    Attributes
    ----------
    icon : str
        a formatted string that points to the icon png file location
    tool_id : str
        the id of the refresh tool used to add to toolbar
    action_text : str
        brief description of the tool's function
	tool_tip: str
		detailed tip about the tool's function
	status_tip: str
		message about tool's status
	shortcut: char
		character that can toggle the tool from keyboard
	-------
    Methods
    -------
     __init__(self,viewer):
	 	connects the StatsDataViewerviewer to the tool
	activate(self):
		action performed when tool is activated

    """
	
	icon = COLLAPSE_LOGO
	tool_id = 'stats:collapse'
	action_text = 'Collapse All'
	tool_tip = 'Collapse All'
	status_tip = 'Collapse All'
	shortcut = 'x'

	def __init__(self, viewer):
		self.viewer = viewer
		
	def close(self):
		pass
	
	def activate(self):
		self.viewer.minimizeLevel()
		'''
		if self.viewer.tabs.currentIndex() == 0:
			self.viewer.subsetTree.collapseAll()
		elif self.viewer.tabs.currentIndex() == 1:
			self.viewer.componentTree.collapseAll()
		'''

@viewer_tool
class Instructions(Tool):
	"""
    A class used to show the instructions for the Statsviewer in a popup window
    ----------
    Attributes
    ----------
    icon : str
        a formatted string that points to the icon png file location
    tool_id : str
        the id of the refresh tool used to add to toolbar
    action_text : str
        brief description of the tool's function
	tool_tip: str
		detailed tip about the tool's function
	status_tip: str
		message about tool's status
	shortcut: char
		character that can toggle the tool from keyboard
	-------
    Methods
    -------
     __init__(self,viewer):
	 	connects the StatsDataViewerviewer to the tool
	activate(self):
		action performed when tool is activated

    """
	icon = INSTRUCTIONS_LOGO
	tool_id = 'stats:instructions'
	action_text = 'Instructions'
	tool_tip = 'Click to see Instructions'
	status_tip = 'Click to see Instructions'
	shortcut = 'I'

	def __init__(self,viewer):
		self.viewer = viewer

	def activate(self):
		#self.icon = '/Users/jk317/Glue/icons/glue_scientific_notation.png'
		#print("Convert button activate")
		self.viewer.showInstructions()

	def close(self):
		pass


@viewer_tool
class Settings(SimpleToolMenu):

	icon = SETTINGS_LOGO
	tool_id = 'stats:settings'
	#action_text = 'Settings'

	#def __init__(self,viewer):
		#super(SelectDecimalPoints, self).__init__(viewer=viewer)
	def menu_actions(self):
		result = []
		#Action for editing decimal points
		action = QtWidgets.QAction("Edit Decimal Points", None)
		action.triggered.connect(self.viewer.showDecimalWindow)
		result.append(action)
		#Action for showing instructions
		action = QtWidgets.QAction("Instructions", None)
		action.triggered.connect(self.viewer.showInstructions)
		result.append(action)
		#Action for toggling automatic calculation
		action = QtWidgets.QAction("Toggle Manual Calculation", None)
		action.triggered.connect(self.viewer.showManualCalc)
		result.append(action)
		return result

	def close(self):
		self.viewer.closeAllWindows


@viewer_tool
class ConvertNotation(Tool):
	"""
	A class used to convert calculated values on the viewer to decimal or
	scientific notation
	----------
	Attributes
	----------
	icon : str
	a formatted string that points to the icon png file location
	tool_id : str
	the id of the refresh tool used to add to toolbar
	action_text : str
	brief description of the tool's function
	tool_tip: str
		detailed tip about the tool's function
	status_tip: str
		message about tool's status
	shortcut: char
		character that can toggle the tool from keyboard
	-------
	Methods
	-------
	__init__(self,viewer):
		connects the StatsDataViewerviewer to the tool
	activate(self):
		action performed when tool is activated

	"""
	icon = NOTATION_LOGO
	tool_id = 'stats:notation_tool'
	action_text = 'Convert'
	tool_tip = 'Click icon to toggle Scientific noation or decimal'
	status_tip = 'Click to toggle notation'
	shortcut = 'N'

	def __init__(self,viewer):
		self.viewer = viewer

	def activate(self):
		#self.icon = '/Users/jk317/Glue/icons/glue_scientific_notation.png'
		#print("Convert button activate")
		self.viewer.pressedEventConvertNotation(not self.viewer.isSci)

	def close(self):
		pass
	
	
	
	

@viewer_tool
class SaveButton(SimpleToolMenu):
	"""
    A class used to export calculated values of the active viewer
    ----------
    Attributes
    ----------
    icon : str
        a formatted string that points to the icon png file location
    tool_id : str
        the id of the refresh tool used to add to toolbar
    action_text : str
        brief description of the tool's function
	tool_tip: str
		detailed tip about the tool's function
	status_tip: str
		message about tool's status
	shortcut: char
		character that can toggle the tool from keyboard
	-------
    Methods
    -------
     __init__(self,viewer):
	 	connects the StatsDataViewerviewer to the tool
	activate(self):
		action performed when tool is activated

    """
	icon = SAVE_LOGO
	tool_id = 'stats:save_tool'
	#action_text = 'Export'
	tool_tip = 'Click icon to export'
	status_tip = 'Click to export'
	shortcut = 'F'

	#def __init__(self,viewer):
	#	self.viewer = viewer

	def menu_actions(self):
		result = []
		#Action for editing decimal points
		action = QtWidgets.QAction("Export Data", None)
		action.triggered.connect(self.viewer.pressedEventExport)
		result.append(action)
		#Action for toggling automatic calculation
		action = QtWidgets.QAction("Save to Data Collection", None)
		action.triggered.connect(self.viewer.pressedEventSaveToDC)
		result.append(action)
		return result

	'''
	def activate(self):
		#print("Export button activate")
		self.viewer.pressedEventExport()
		#print(self.viewer.layers[0].layer)
	'''

	def close(self):
		pass
	
	

@viewer_tool
class HomeButton(Tool):
	"""
	A class used to restore the viewer to its default state
	----------
	Attributes
	----------
	icon : str
	a formatted string that points to the icon png file location
	tool_id : str
	the id of the refresh tool used to add to toolbar
	action_text : str
	brief description of the tool's function
	tool_tip: str
		detailed tip about the tool's function
	status_tip: str
		message about tool's status
	shortcut: char
		character that can toggle the tool from keyboard
	-------
	Methods
	-------
	__init__(self,viewer):
		connects the StatsDataViewerviewer to the tool
	activate(self):
		action performed when tool is activated

	"""
	icon = HOME_LOGO
	tool_id = 'stats:home_tool'
	action_text = 'Home'
	tool_tip = 'Click to return to home'
	status_tip = 'Click to return to home'
	shortcut = 'H'

	def __init__(self, viewer):
		self.viewer = viewer

	def activate(self):
		self.viewer.homeButtonEvent()

	def close(self):
		pass
	

@viewer_tool
class ExpandButton(Tool):
	"""
    A class used to expand all items in the viewer
    ----------
    Attributes
    ----------
    icon : str
        a formatted string that points to the icon png file location
    tool_id : str
        the id of the refresh tool used to add to toolbar
    action_text : str
        brief description of the tool's function
	tool_tip: str
		detailed tip about the tool's function
	status_tip: str
		message about tool's status
	shortcut: char
		character that can toggle the tool from keyboard
	-------
    Methods
    -------
     __init__(self,viewer):
	 	connects the StatsDataViewerviewer to the tool
	activate(self):
		action performed when tool is activated

    """
	icon = EXPAND_LOGO
	tool_id = 'stats:expand_tool'
	action_text = 'expand'
	tool_tip = 'Click to expand all data and subsets'
	status_tip = 'Click to expand'
	shortcut = 'E'

	def __init__(self, viewer):
		self.viewer = viewer
		self.toExpand = True

	def activate(self):
		'''
		if self.viewer.tabs.currentIndex() == 0:
			self.viewer.subsetTree.expandAll()
		elif self.viewer.tabs.currentIndex() == 1:
			self.viewer.componentTree.expandAll()
		'''
		self.viewer.expandLevel()
		#self.viewer.expandAll(self.toExpand)
		#self.toExpand = not self.toExpand

	def close(self):
		pass


@viewer_tool
class CalculateButton(Tool):
	"""
    A class used to calculate values that are checked on the viewer
    ----------
    Attributes
    ----------
    icon : str
        a formatted string that points to the icon png file location
    tool_id : str
        the id of the refresh tool used to add to toolbar
    action_text : str
        brief description of the tool's function
	tool_tip: str
		detailed tip about the tool's function
	status_tip: str
		message about tool's status
	shortcut: char
		character that can toggle the tool from keyboard
	-------
    Methods
    -------
     __init__(self,viewer):
	 	connects the StatsDataViewerviewer to the tool
	activate(self):
		action performed when tool is activated

    """
	icon = CALCULATE_LOGO
	tool_id = 'stats:calc_tool'
	action_text = 'Calculate'
	tool_tip = 'Click side icons to calculate'
	status_tip = 'Click to calculate'
	shortcut = 'C'

	def __init__(self, viewer):
		self.viewer = viewer

	def activate(self):
		#print("Calculate button activate")
		self.viewer.calculateAll()
		#print(self.viewer.layers[0].layer)

	def close(self):
		pass

@viewer_tool
class SortButton(Tool):
	"""
	A class used to sort calculated values 
	----------
	Attributes
	----------
	icon : str
	a formatted string that points to the icon png file location
	tool_id : str
	the id of the refresh tool used to add to toolbar
	action_text : str
	brief description of the tool's function
	tool_tip: str
		detailed tip about the tool's function
	status_tip: str
		message about tool's status
	shortcut: char
		character that can toggle the tool from keyboard
	-------
	Methods
	-------
	__init__(self,viewer):
		connects the StatsDataViewerviewer to the tool
	activate(self):
		action performed when tool is activated

	"""
	icon = SORT_LOGO
	tool_id = 'stats:sort_tool'
	action_text = 'Sort'
	tool_tip = 'Click side icons to sort'
	status_tip = 'Choose a column to sort by. When you are done, deactivate sort mode.'
	shortcut = 'S'

	def __init__(self, viewer):
		#super(Tool, self).__init__(viewer)
		 self.viewer = viewer

	def activate(self):
		if self.viewer.tabs.currentIndex() == 0:
			if self.viewer.subsetTree.isSortingEnabled():
				self.viewer.subsetTree.setSortingEnabled(False)
			else:
				self.viewer.subsetTree.setSortingEnabled(True)
		elif self.viewer.tabs.currentIndex() == 1:
			if self.viewer.componentTree.isSortingEnabled():
				self.viewer.componentTree.setSortingEnabled(False)
			else:
				self.viewer.componentTree.setSortingEnabled(True)

	def close(self):
		pass
	
@viewer_tool
class ExportButton(Tool):
	"""
    A class used to export calculated values of the active viewer
    ----------
    Attributes
    ----------
    icon : str
        a formatted string that points to the icon png file location
    tool_id : str
        the id of the refresh tool used to add to toolbar
    action_text : str
        brief description of the tool's function
	tool_tip: str
		detailed tip about the tool's function
	status_tip: str
		message about tool's status
	shortcut: char
		character that can toggle the tool from keyboard
	-------
    Methods
    -------
     __init__(self,viewer):
	 	connects the StatsDataViewerviewer to the tool
	activate(self):
		action performed when tool is activated

    """
	icon = EXPORT_LOGO
	tool_id = 'stats:export_tool'
	action_text = 'Export'
	tool_tip = 'Click icon to export'
	status_tip = 'Click to export'
	#shortcut = 'M'

	def __init__(self,viewer):
		self.viewer = viewer

	def activate(self):
		#print("Export button activate")
		self.viewer.pressedEventExportToViewer()
		#print(self.viewer.layers[0].layer)

	def close(self):
		pass
