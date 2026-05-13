require 'liquid'

module Jekyll
  module RegexFilters
    # search string for regex capture group, return first or all matches
    def regex_scan(string, search, multi = false, all = false)
      return "" if string.nil?
      regex = multi ? /#{search}/m : /#{search}/
      matches = string.scan(regex).flatten
      if matches.length
        return all ? matches : matches[0]
      else
        return ""
      end
    end

    # find regex capture group in string and replace 
    def regex_replace(string, search, replace)
      return "" if string.nil?
      # Convert $1, $2, etc. to \1, \2 for Ruby gsub compatibility
      ruby_replace = replace.gsub(/\$(\d+)/, '\\\\\1')
      return string.gsub(Regexp.new(search, Regexp::MULTILINE), ruby_replace)
    end

    # strip all non-letter and non-number characters from string
    def regex_strip(string)
      return "" if string.nil?
      return string.gsub(/[^\p{L}\p{N}.,;:-]/u, " ").gsub(/\s+/, " ").strip
    end
  end
end

Liquid::Template.register_filter(Jekyll::RegexFilters)
