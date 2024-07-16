import "./index.less";

import { ExpandableRowContent, Td, Tr } from "@patternfly/react-table";

import RowContent from "@/components/molecules/ExpandedRow";
import TableCell from "@/components/atoms/TableCell";
import { uid } from "@/utils/helper.js";

const TableRows = (props) => {
  const { rows, columns, addExpansion } = props;

  return (
    rows?.length > 0 &&
    rows.map((item, rowIndex) => {
      return (
        <>
          <Tr key={uid()}>
            {addExpansion && (
              <Td
                expand={{
                  rowIndex,
                  isExpanded: props?.isRunExpanded(item),
                  onToggle: () =>
                    props?.setRunExpanded(item, !props?.isRunExpanded(item)),
                  expandId: `expandable-row${uid()}`,
                }}
              />
            )}

            {columns.map((col) => (
              <TableCell key={uid()} col={col} item={item} />
            ))}
          </Tr>
          {addExpansion && (
            <Tr isExpanded={props?.isRunExpanded(item)}>
              <Td colSpan={8}>
                <ExpandableRowContent>
                  <RowContent
                    item={item}
                    graphData={props.graphData}
                    type={props.type}
                  />
                </ExpandableRowContent>
              </Td>
            </Tr>
          )}
        </>
      );
    })
  );
};

export default TableRows;