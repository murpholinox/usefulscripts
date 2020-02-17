## What it does: Finds all PDBs with 95% sequence id to hen egg white lysozyme that have been resolved using X-RAY
## From: http://www.rcsb.org/pdb/software/static.do?p=/software/webservices/search_nmr.jsp and murpholinox@gmail.com
## Usage: `python2 ./pdb_fetch_seq_xray_p2.py`
## Output: Number of PDB IDs that conform to the search criteria
## Works with: python2

import urllib2


url = 'http://www.rcsb.org/pdb/rest/search'

queryText = """

<orgPdbCompositeQuery version="1.0">
 <queryRefinement>
  <queryRefinementLevel>0</queryRefinementLevel>
  <orgPdbQuery>
    <version>head</version>
    <queryType>org.pdb.query.simple.SequenceQuery</queryType>
    <description>SEQUENCE P00698</description>
    <sequence>KVFGRCELAAAMKRHGLDNYRGYSLGNWVCAAKFESNFNTQATNRNTDGSTDYGILQINSRWWCNDGRTPGSRNLCNIPCSALLSSDITASVNCAKKIVSDGNGMNAWVAWRNRCKGTDVQAWIRGCRL</sequence>
    <searchTool>psiblast</searchTool>
    <maskLowComplexity>yes</maskLowComplexity>
    <eValueCutoff>10.0</eValueCutoff>
    <sequenceIdentityCutoff>95</sequenceIdentityCutoff>
  </orgPdbQuery>
 </queryRefinement>
 <queryRefinement>
  <queryRefinementLevel>1</queryRefinementLevel>
  <conjunctionType>and</conjunctionType>
  <orgPdbQuery>
    <version>head</version>
    <queryType>org.pdb.query.simple.ExpTypeQuery</queryType>
    <description>X-RAY with Data</description>
    <mvStructure.expMethod.value>X-RAY</mvStructure.expMethod.value>
    <mvStructure.hasExperimentalData.value>Y</mvStructure.hasExperimentalData.value>
  </orgPdbQuery>
 </queryRefinement>
</orgPdbCompositeQuery>

"""


print "query:\n", queryText

print "querying PDB...\n"

req = urllib2.Request(url, data=queryText)

f = urllib2.urlopen(req)

result = f.read()


if result:

   # print "Found number of PDB entries:", result.count('\n')

else:

    print "Failed to retrieve results"
