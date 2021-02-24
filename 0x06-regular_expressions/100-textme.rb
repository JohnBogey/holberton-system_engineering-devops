#!/usr/bin/env ruby
puts ARGV[0].scan(/om:(\w*)[^\w]*to:(\+?\w*)[^\w]*flags:([^\]]*)/).join(',')
