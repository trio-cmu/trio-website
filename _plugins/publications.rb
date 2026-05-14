# Jekyll plugin to filter publications by project
module PublicationsFilter
  def publications_for_project(publications_data, project_permalink, metadata)
    # Build a lookup map of publication id -> projects
    metadata_by_id = {}
    if metadata.is_a?(Array)
      metadata.each do |entry|
        if entry['id'].is_a?(String)
          metadata_by_id[entry['id']] = entry['projects'] || []
        end
      end
    end
    
    # Filter publications for this project
    results = publications_data.select do |pub|
      pub_id = pub['id']
      projects = metadata_by_id[pub_id] || []
      projects.include?(project_permalink)
    end

    # Sort by date (newest first). Dates are expected as YYYY-MM-DD strings;
    # fall back to earliest date when parsing fails or date missing.
    require 'date'
    results.sort_by do |pub|
      begin
        Date.parse(pub['date'].to_s)
      rescue
        Date.new(0)
      end
    end.reverse
  end
end

Liquid::Template.register_filter(PublicationsFilter)
