## What it does: Finds all PDBs that have been resolved for a particular organism
## From: http://www.rcsb.org/pdb/software/static.do?p=/software/webservices/search_organism.jsp
## Usage: `perl ./pdb_fetch_organism.pl` 
## Output: List of PDB IDs that conform to the search criteria
## Works with: perl5

use strict;
use LWP::Simple qw( $ua );


# Change the $organism_name variable to get another organism
my $organism_name = 'nipah';
my $XML_query = qq(
<?xml version="1.0" encoding="UTF-8"?>

<orgPdbQuery>
 <version>B0905</version>
 <queryType>org.pdb.query.simple.OrganismQuery</queryType>
 <description>Organism Search: Organism Name=$organism_name </description>

 <organismName>$organism_name</organismName>
</orgPdbQuery>
);
print "\nquery:", $XML_query;

# you can configure a proxy...                                                                          
#$ua->proxy( http => 'http://yourproxy:8080' );

# Create a request                                                                                  

my $request = HTTP::Request->new( POST => 'http://www.rcsb.org/pdb/rest/search/');


$request->content_type( 'application/x-www-form-urlencoded' );

$request->content( $XML_query );

# Post the XML query                                                                                
print "\n querying PDB...";
print "\n";

print $XML_query;
my $response = $ua->request( $request );


# Check to see if there is an error
unless( $response->is_success ) {
    print "\n an error occurred: ", $response->status_line, "\n";

}

# Print response content in either case

print "\n response content:\n", $response->content;
