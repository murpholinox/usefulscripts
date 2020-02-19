## What it does: Finds all PDBs from the top proteins overpopulating the PDB that have been resolved using X-RAY
## From: http://www.rcsb.org/pages/webservices/python3_search_nmr and murpholinox@gmail.com
## Usage: `python ./pdb_fetch_uacs_ent1_xray.py`
## Output: List of PDB IDs that conform to the search criteria
## Works with: python3

import requests

if __name__ == '__main__':
    url = 'http://www.rcsb.org/pdb/rest/search'

    query_text = """
<orgPdbCompositeQuery version="1.0">
 <queryRefinement>
  <queryRefinementLevel>0</queryRefinementLevel>
  <orgPdbQuery>
    <version>head</version>
    <queryType>org.pdb.query.simple.UpAccessionIdQuery</queryType>
    <description>Simple query for a list of Uniprot Accession IDs: </description>
    <accessionIdList>P00698 P61769 P00918 P00720 P11838	P00760 P24941 P00734 P56817 P06746 P42212 O60885 P02766	P04439 Q6PJP8 O95696 P02185 P07900 Q15596 P61823 P01887	P03372 P00644 P69905 P0AEX9 P29476 Q6B0I6 P68871 P01308	P18031 Q9UIF8 P68431 Q16539 P19491 P37231 P00489 Q15788	P0CG48 P61626 P22629 P01889 P00533 P00800 P62805 P04637	P00431 P0ABE7</accessionIdList>
  </orgPdbQuery>
 </queryRefinement>
 <queryRefinement>
  <queryRefinementLevel>1</queryRefinementLevel>
  <conjunctionType>and</conjunctionType>
  <orgPdbQuery>
    <version>head</version>
    <queryType>org.pdb.query.simple.NumberOfEntitiesQuery</queryType>
    <description>Number of Entities Search : Entity Type=Protein Min Number of Entities=1 Max Number of Entities=1</description>
    <entity.type.>p</entity.type.>
    <struct_asym.numEntities.min>1</struct_asym.numEntities.min>
    <struct_asym.numEntities.max>1</struct_asym.numEntities.max>
  </orgPdbQuery>
 </queryRefinement>
 <queryRefinement>
  <queryRefinementLevel>2</queryRefinementLevel>
  <conjunctionType>and</conjunctionType>
  <orgPdbQuery>
    <version>head</version>
    <queryType>org.pdb.query.simple.ExpTypeQuery</queryType>
    <description>Experimental Method is X-RAY</description>
    <mvStructure.expMethod.value>X-RAY</mvStructure.expMethod.value>
    <mvStructure.expMethod.exclusive>y</mvStructure.expMethod.exclusive>
  </orgPdbQuery>
 </queryRefinement>
</orgPdbCompositeQuery>


"""

    print("Query: %s" % query_text)
    print("Querying RCSB PDB REST API...")

    header = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=query_text, headers=header)

    if response.status_code == 200:
        print("Found %d PDB entries matching query." % len(response.text))
        print("Matches: \n%s" % response.text)
    else:
        print("Failed to retrieve results")



