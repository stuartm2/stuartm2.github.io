
module Jekyll
    module LocalFilters
        def strip_tag_prefix(title, tag)
            if tag.kind_of?(Array)
                t = tag[0]
            else
                t = tag
            end

            if title != nil and t != nil and title.downcase.start_with? t.downcase + ":"
                return title[(t.length + 1)..-1].strip
            end

            return title
        end
    end
end

Liquid::Template.register_filter(Jekyll::LocalFilters)
