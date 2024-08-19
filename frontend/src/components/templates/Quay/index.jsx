import { fetchQuayJobsData, setSelectedFilter } from "@/actions/quayActions.js";
import { useDispatch, useSelector } from "react-redux";
import { useEffect, useMemo } from "react";

import MetricsTab from "@/components/organisms/MetricsTab";
import TableFilter from "@/components/organisms/TableFilters";
import TableLayout from "@/components/organisms/TableLayout";
import { useNavigate } from "react-router-dom";

const Quay = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const {
    tableData,
    tableColumns,
    activeSortIndex,
    activeSortDir,
    page,
    perPage,
    filteredResults,
    tableFilters,
    filterOptions,
    categoryFilterValue,
    filterData,
    appliedFilters,
    start_date,
    end_date,
    selectedFilters,
    summary,
  } = useSelector((state) => state.quay);

  useEffect(() => {
    dispatch(fetchQuayJobsData());
  }, [dispatch]);

  //Filter Helper
  const modifidedTableFilters = useMemo(
    () =>
      tableFilters.filter(
        (item) => item.value !== "endDate" && item.value !== "startDate"
      ),
    [tableFilters]
  );
  const updateSelectedFilter = (category, value, isFromMetrics) => {
    dispatch(setSelectedFilter(category, value, isFromMetrics));
  };
  //Filter Helper

  return (
    <>
      <MetricsTab
        totalItems={filteredResults.length}
        summary={summary}
        updateSelectedFilter={updateSelectedFilter}
        navigation={navigate}
        type={"quay"}
        appliedFilters={appliedFilters}
      />
      <TableFilter
        tableFilters={modifidedTableFilters}
        filterOptions={filterOptions}
        categoryFilterValue={categoryFilterValue}
        filterData={filterData}
        appliedFilters={appliedFilters}
        start_date={start_date}
        end_date={end_date}
        type={"quay"}
        selectedFilters={selectedFilters}
        updateSelectedFilter={updateSelectedFilter}
        showColumnMenu={false}
        navigation={navigate}
      />
      <TableLayout
        tableData={tableData}
        tableColumns={tableColumns}
        activeSortIndex={activeSortIndex}
        activeSortDir={activeSortDir}
        page={page}
        perPage={perPage}
        totalItems={filteredResults.length}
        type={"quay"}
        addExpansion={false}
      />
    </>
  );
};

export default Quay;
