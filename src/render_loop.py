#!/usr/bin/env python3
"""Main render loop"""

from OpenGL.GL import GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, glClear

def setup_render_loop(window, fps_display):
	"""Define render loop"""
	@window.event
	def on_draw():
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		fps_display.draw()
