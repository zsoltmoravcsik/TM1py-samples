"""
Create MDX View on }ClientGroups cube and query data through it.

IMPORTANT: MDX Views can not be seen through Architect/Perspectives.
"""

import uuid

from TM1py.Objects import MDXView
from TM1py.Services import TM1Service


with TM1Service(address='localhost', port=12354, user='admin', password='apple', ssl=True) as tm1:
    # Random text
    random_string = str(uuid.uuid4())

    # Create mdx view
    mdx = "SELECT " \
          "NON EMPTY {TM1SUBSETALL( [}Clients] )} on ROWS, " \
          "NON EMPTY {TM1SUBSETALL( [}Groups] )} ON COLUMNS " \
          "FROM [}ClientGroups]"
    mdx_view = MDXView(cube_name='}ClientGroups', view_name='TM1py_' + random_string, MDX=mdx)

    # Create mdx view on TM1 Server
    tm1.cubes.views.create(view=mdx_view)

    # Get view content
    content = tm1.cubes.cells.get_view_content(cube_name=mdx_view.cube, view_name=mdx_view.name)

    # Print content
    print(content)



