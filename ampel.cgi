#!/usr/bin/env ruby
# frozen_string_literal: true

require 'cgi'

STATE_COLORS = { red: '#A90533', green: '#4CB432' }
STATE_COLORS.default = '#000000'

cgi = CGI.new('html5')

state = File.read('status').chomp.to_sym

if cgi['change'].match(/true/)
  state = if state == :red then :green else :red end
  File.write('status', state.to_s)
end

cgi.out do
  File.open('template.html').read.force_encoding('utf-8').gsub(/STATE_COLOR_NAME/, state.to_s).gsub(/STATE_COLOR/, STATE_COLORS[state])
end
